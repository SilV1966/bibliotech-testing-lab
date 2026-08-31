from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "template_aluno"

ERROS = []


def ok(mensagem):
    print(f"[OK] {mensagem}")


def erro(mensagem):
    ERROS.append(mensagem)
    print(f"[ERRO] {mensagem}")


print("=" * 60)
print("VALIDADOR — MISSÃO QA BIBLIOTECH")
print("=" * 60)


# ------------------------------------------------------------
# 1. Verificar estrutura
# ------------------------------------------------------------

arquivos_obrigatorios = [
    "README.md",
    "requisitos.md",
    "requirements-dev.txt",
    "pytest.ini",
    "src/bibliotech.py",
    "tests/test_smoke.py",
    "docs/plano_testes.md",
    "docs/roteiro_testes.md",
    "docs/matriz_rastreabilidade.md",
    ".github/pull_request_template.md",
    ".github/workflows/testes.yml",
]

for arquivo in arquivos_obrigatorios:
    caminho = TEMPLATE / arquivo

    if caminho.exists():
        ok(f"Arquivo encontrado: {arquivo}")
    else:
        erro(f"Arquivo ausente: {arquivo}")


# ------------------------------------------------------------
# 2. Procurar pistas proibidas
# ------------------------------------------------------------

palavras_proibidas = [
    "defeito proposital",
    "bug aqui",
    "erro nesta condição",
    "gabarito",
    "deveria usar >=",
]

for arquivo in TEMPLATE.rglob("*"):
    if not arquivo.is_file():
        continue

    try:
        texto = arquivo.read_text(encoding="utf-8").lower()
    except UnicodeDecodeError:
        continue

    for termo in palavras_proibidas:
        if termo in texto:
            erro(
                f"Pista potencial encontrada em "
                f"{arquivo.relative_to(TEMPLATE)}: {termo}"
            )


if not ERROS:
    ok("Nenhuma pista proibida encontrada.")


# ------------------------------------------------------------
# 3. Verificar comportamento do módulo
# ------------------------------------------------------------

sys.path.insert(0, str(TEMPLATE))

try:
    from src.bibliotech import pode_emprestar

    if pode_emprestar(True, False, 2) is True:
        ok("RF01: usuário com 2 empréstimos é permitido.")
    else:
        erro("Comportamento inesperado para 2 empréstimos.")

    # O defeito didático precisa continuar presente.
    if pode_emprestar(True, False, 3) is True:
        ok("Defeito didático confirmado no limite de 3 empréstimos.")
    else:
        erro(
            "O defeito didático aparentemente foi corrigido. "
            "Restaurar o template antes da aula."
        )

    if pode_emprestar(True, False, 4) is False:
        ok("RF01: usuário com 4 empréstimos é recusado.")
    else:
        erro("Comportamento inesperado para 4 empréstimos.")

except Exception as exc:
    erro(f"Não foi possível importar/testar bibliotech.py: {exc}")


# ------------------------------------------------------------
# 4. Executar smoke test
# ------------------------------------------------------------

try:
    resultado = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=TEMPLATE,
        capture_output=True,
        text=True,
        timeout=30,
    )

    print("\nResultado do pytest:")
    print(resultado.stdout)

    if resultado.returncode == 0:
        ok("Smoke test executado com sucesso.")
    else:
        erro("Smoke test falhou.")
        print(resultado.stderr)

except FileNotFoundError:
    erro("pytest não está instalado.")

except subprocess.TimeoutExpired:
    erro("pytest excedeu o tempo limite.")


# ------------------------------------------------------------
# Resultado
# ------------------------------------------------------------

print()
print("=" * 60)

if ERROS:
    print("VALIDAÇÃO REPROVADA")
    print()

    for item in ERROS:
        print(f"- {item}")

    print("=" * 60)
    sys.exit(1)

print("VALIDAÇÃO CONCLUÍDA COM SUCESSO")
print("Template pronto para a aula.")
print("=" * 60)

sys.exit(0)
