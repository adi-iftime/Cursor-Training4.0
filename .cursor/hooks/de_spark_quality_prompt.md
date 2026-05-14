You are reviewing a pending PySpark / Databricks pipeline edit.

Using the hook JSON input (`$ARGUMENTS` is replaced with the full payload), confirm:

- partitioning and table/file layout match expected volume and SLA
- shuffle-heavy joins are bounded and justified
- schema evolution and null handling are explicit across bronze → silver → gold

If the change is acceptable, allow. If not, deny with concrete remediation steps.
