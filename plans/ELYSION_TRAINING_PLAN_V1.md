# ELYSION training plan V1

Status: PROPOSED / NON_EXECUTED / WEIGHTS_CHANGED=false

1. Pin base model revision and approve license.
2. Build ELYSION-GOLD-V1 with immutable lineage and strict train/validation/M6 separation.
3. Run and reproduce the base-model cold baseline.
4. Run a reversible LoRA/QLoRA pilot only if all gates pass.
5. Evaluate the unchanged M6 set, transfer, calibration, regressions, tool use and latency.
6. Red-team and reproduce before promote-or-rollback.

Initial pilot envelope, not authorization: 500–1000 GOLD samples, one epoch, LoRA rank 16, alpha 32, dropout 0.05, learning rate 1e-4, sequence length 2048. Hyperparameters remain subject to measured compute and candidate architecture.

Success requires an actual adapter/weight artifact SHA, dataset SHA, training config, seed, checkpoint, baseline M6, post-training M6, transfer and regression results.

