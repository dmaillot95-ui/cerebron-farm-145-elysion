# ELYSION architecture V1

Status: PROPOSED / NON_EXECUTED

ELYSION is a language model plus a versioned adapter, assisted at inference time by CÉRÉBRON. CÉRÉBRON remains the orchestrator and owns coalition selection, tools, memory policy, evidence, and final audit.

The first experiment keeps the selected base tokenizer and architecture unchanged, creates one reversible `elysion-core-lora` adapter, and exposes it through the model router. SAPHEA, SPIRALION, ETHERION, HYPERION, ASTRION, METRION, AFAH, AÉLYS and ELYRA remain logical capabilities until a real worker/model binding is proven.

Flow: user → AÉLYS → CÉRÉBRON → ELYSION/base candidate → minimal specialist coalition → tools → AFAH/red team → evidence → memory.

Failure is closed: unavailable models, workers, tools, memories or engines are reported as unavailable rather than replaced by static output.

