# neighbor-context-detection-evaluation

Evaluation of whether extended neighbor node context improves ML-based attack detection in distributed networks.

## Research Question

Does incorporating aggregated threat reports from neighboring nodes improve a machine learning classifier's ability to detect whether node X is under attack or behaving benignly — compared to a classifier that relies solely on the node's own local data?

## Approach

Two ML classifiers are trained and evaluated:

| Model | Input |
|-------|-------|
| **Baseline** | Local threat report of node X only |
| **Context-extended** | Local threat report of node X + aggregated neighbor node context |

Both models perform binary classification: `attack` vs. `benign`.

## Background

The underlying infrastructure was designed and implemented in a preceding research work. Each node in the distributed network generates standardized CTI threat reports and distributes them to neighboring nodes via a private peer-to-peer network. A weighted aggregation mechanism consolidates the variable number of incoming neighbor reports into a fixed-size feature vector, which serves as extended context input for the classifier.

This repository contains the evaluation paper, experiment code, and related artifacts that assess the detection improvement achieved through this collaborative, context-extended approach.

## Repository Contents

- `paper/` — Research paper drafts and final document
- `src/` — ML model implementations (baseline and context-extended)
- `evaluation/` — Experiment scripts, metrics, and result analysis
- `data/` — Dataset references and preprocessing scripts
- `docs/` — Figures, architecture diagrams, and notes

## Status

Work in progress — paper and evaluation under active development.

