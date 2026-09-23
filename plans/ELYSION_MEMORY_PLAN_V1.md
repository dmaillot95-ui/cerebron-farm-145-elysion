# ELYSION memory plan V1

Status: PROPOSED / EXTERNAL DATA PLANES NOT VERIFIED THIS CYCLE

- M0 ephemeral; M1 trace; M2 replay; M3 warm; M4 GOLD; M5 model/adapter; M6 cold benchmark; M7 evidence.
- M6 is sealed and denied to training, RAG, teacher generation and prompt construction.
- GitHub stores code, manifests, SHAs, provenance and small receipts, not large model/data payloads.
- Candidate durable routes are the declared private Hugging Face memory repositories, but live access must be revalidated before use.
- Every seed follows RAW → QUARANTINE → DEDUP → AUDIT → COUNTER-AUDIT → RED TEAM → REPRODUCTION → GOLD or RED.
- AGORA capsules never enter training automatically.

