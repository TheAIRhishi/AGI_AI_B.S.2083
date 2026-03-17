# Security Policy

## Data Provenance
- All data sources must be documented in `data/README.md`
- Include source URLs and access dates
- Document any licensing requirements

## Model Integrity
- All trained models must be versioned
- Store model metadata with checkpoints
- Document hyperparameters used

## Reproducibility
- Pin all dependency versions exactly
- Document random seeds used
- Include hardware specifications

## Audit Trail
- All changes tracked through git commits
- All major decisions documented in issues/discussions
- Reproducibility verified by CI/CD pipeline