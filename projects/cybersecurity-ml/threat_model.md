# Defensive Threat Model

## Protected objective
Identify anomalous security telemetry early enough to support defensive review while minimizing unnecessary alerts.

## Observable signals
Authentication failures, connection volume, destination diversity, bytes transferred, session duration, off-hours activity, privilege-sensitive activity, and deviation from a user's historical baseline.

## Evaluated risks
- anomalous account activity
- unusual connection behavior
- suspicious privilege-sensitive events
- operational overload from false positives
- brittle model behavior caused by overreliance on a small number of features

## Scope boundary
This repository evaluates defensive detection only. It does not provide instructions for intrusion, exploitation, credential acquisition, malware, persistence, or detection evasion.
