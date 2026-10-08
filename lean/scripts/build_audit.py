#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the complete proof and freshly audit all exported theorem/lemma axioms."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, subprocess, time

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


def main():
    evidence = ROOT / '.lake/verification'
    evidence.mkdir(exist_ok=True)
    sources = [ROOT / 'CommutingConvergence.lean', ROOT / 'verification/Axioms.lean',
                ROOT / 'verification/FCTargetProofs.lean']
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    for p in sources:
        if re.search(r'\b(?:sorry|admit|native_decide)\b|^\s*(?:axiom|opaque)\b', p.read_text(), re.M):
            raise SystemExit('Unexpected proof placeholder or axiom: ' + str(p))
    started = time.monotonic()
    with (evidence / 'build.log').open('w') as log:
        built = subprocess.run(['lake', 'build', 'CommutingConvergence'], cwd=ROOT,
                               stdout=log, stderr=subprocess.STDOUT)
    if built.returncode:
        raise SystemExit('Project build failed; see evidence/build.log')
    with (evidence / 'axioms.log').open('w') as log:
        audited = subprocess.run(['lake', 'env', 'lean', '-DautoImplicit=false', 'verification/Axioms.lean'],
                                 cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
    if audited.returncode:
        raise SystemExit('Fresh axiom audit failed; see evidence/axioms.log')
    expected = re.findall(r'^#print axioms (.+)$', (ROOT / 'verification/Axioms.lean').read_text(), re.M)
    reports = re.findall(r"^'(.+)' depends on axioms: \[([^\]]*)\]", (evidence / 'axioms.log').read_text(), re.M)
    if len(reports) != len(expected) or {name for name, _ in reports} != set(expected):
        raise SystemExit('Fresh audit theorem inventory differs from the declared inventory')
    for name, used in reports:
        if {a.strip() for a in used.split(',') if a.strip()} - ALLOWED:
            raise SystemExit('Unexpected axiom in ' + name)
    with (evidence / 'target-axioms.log').open('w') as log:
        target_audit = subprocess.run(['lake', 'env', 'lean', '-DautoImplicit=false',
            'verification/FCTargetProofs.lean'], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
    target_reports = re.findall(r"^'(.+)' depends on axioms: \[([^\]]*)\]",
        (evidence / 'target-axioms.log').read_text(), re.M)
    target_expected = set(re.findall(r'^#print axioms (.+)$',
        (ROOT / 'verification/FCTargetProofs.lean').read_text(), re.M))
    if target_audit.returncode or len(target_reports) != len(target_expected) or {n for n, _ in target_reports} != target_expected:
        raise SystemExit('Complete target proof audit failed')
    if any({a.strip() for a in used.split(',') if a.strip()} - ALLOWED for _, used in target_reports):
        raise SystemExit('Unexpected axiom in complete target proofs')
    for p in sources:
        if hashlib.sha256(p.read_bytes()).hexdigest() != hashes[str(p.relative_to(ROOT))]:
            raise SystemExit('Source changed during the build: ' + str(p))
    record = {'passed': True, 'completed_at_utc': datetime.now(timezone.utc).isoformat(),
              'toolchain': (ROOT / 'lean-toolchain').read_text().strip(), 'sources': hashes,
              'public_declarations_audited': len(expected),
              'additional_complete_target_axiom_reports': dict(target_reports),
              'FC_statement_placeholders_included_in_proof_audit': False, 'allowed_axioms': sorted(ALLOWED),
              'seconds': time.monotonic() - started,
              'independent_dependency_source_rebuild': False}
    (evidence / 'build-results.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'passed': True, 'sources': len(sources), 'declarations': len(expected)}))


if __name__ == '__main__':
    main()
