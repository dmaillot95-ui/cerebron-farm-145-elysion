import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def test_project_does_not_create_f145():
    project = load("config/elysion-project.json")
    assert project["entity_type"] == "MODEL_PROJECT"
    assert project["farm_id"] is None
    assert project["farm_count_effect"] == 0
    assert project["master_farm_cap"] == 144

def test_training_is_fail_closed():
    project = load("config/elysion-project.json")
    gates = load("config/release-gates.json")
    assert project["training_status"] == "NON_EXECUTED"
    assert project["weights_changed"] is False
    assert gates["decision"] == "NO_GO_TRAINING"
    assert any(g["status"] == "BLOCKED" for g in gates["gates"])

def test_agora_has_exactly_six_astra_functions():
    agora = load("agora/AGORA-ELYSION-001.json")
    assert len(agora["participants"]) == 6
    assert agora["training_executed"] is False
    assert agora["hf_agents_executed"] == []
