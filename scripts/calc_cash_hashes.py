import hashlib

def sha256(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

gestor_keys = ["GESTOR-CASH-2026-X89"]
student_keys = ["ALUNO-CASH-8842-PRO", "ALUNO-CASH-7731-VIP", "CASH-2026-ACESSO-FULL"]

print("=== CASH GESTOR HASHES ===")
for k in gestor_keys:
    clean = k.replace('-', '').replace('_', '').replace(' ', '')
    print(f"'{sha256(k)}', // raw {k}")
    print(f"'{sha256(clean)}', // clean {clean}")

print("\n=== CASH STUDENT HASHES ===")
for k in student_keys:
    clean = k.replace('-', '').replace('_', '').replace(' ', '')
    print(f"'{sha256(k)}', // raw {k}")
    print(f"'{sha256(clean)}', // clean {clean}")
