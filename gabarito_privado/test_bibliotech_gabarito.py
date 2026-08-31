from src.bibliotech import (
    pode_emprestar,
    calcular_multa,
    classificar_atraso,
)


# ==================================================
# RF01 — Permissão para empréstimo
# ==================================================


def test_usuario_sem_emprestimos_pode_emprestar():
    assert pode_emprestar(True, False, 0) is True


def test_usuario_com_dois_emprestimos_pode_emprestar():
    assert pode_emprestar(True, False, 2) is True


def test_usuario_com_tres_emprestimos_nao_pode_emprestar():
    assert pode_emprestar(True, False, 3) is False


def test_usuario_com_quatro_emprestimos_nao_pode_emprestar():
    assert pode_emprestar(True, False, 4) is False


def test_usuario_inativo_nao_pode_emprestar():
    assert pode_emprestar(False, False, 0) is False


def test_usuario_com_pendencia_nao_pode_emprestar():
    assert pode_emprestar(True, True, 0) is False


# ==================================================
# RF02 — Multa
# ==================================================


def test_atraso_negativo_nao_gera_multa():
    assert calcular_multa(-1) == 0.0


def test_atraso_zero_nao_gera_multa():
    assert calcular_multa(0) == 0.0


def test_um_dia_de_atraso():
    assert calcular_multa(1) == 2.0


def test_sete_dias_de_atraso():
    assert calcular_multa(7) == 14.0


def test_oito_dias_de_atraso():
    assert calcular_multa(8) == 17.0


# ==================================================
# RF03 — Classificação
# ==================================================


def test_zero_dias_sem_atraso():
    assert classificar_atraso(0) == "sem atraso"


def test_um_dia_atraso_leve():
    assert classificar_atraso(1) == "atraso leve"


def test_sete_dias_atraso_leve():
    assert classificar_atraso(7) == "atraso leve"


def test_oito_dias_atraso_moderado():
    assert classificar_atraso(8) == "atraso moderado"


def test_trinta_dias_atraso_moderado():
    assert classificar_atraso(30) == "atraso moderado"


def test_trinta_um_dias_atraso_grave():
    assert classificar_atraso(31) == "atraso grave"
