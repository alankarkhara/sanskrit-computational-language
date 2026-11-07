# SCL v0.9.0 — Guided nonprogrammer task interface (restricted pilot)

The new deterministic request front end understands only explicit *count tokens in <registered-id>* requests. Requests for "words" trigger clarification because counting words is not identical to whitespace-token counting. Unsupported requests fail closed. Every accepted request produces a readable contract preview and a native SCL source contract. A distinct approval step is mandatory. The implementation does not execute external actions, interpret arbitrary language, or authenticate a real person merely from approval=True.

Run: `python guided090_cli.py "Count tokens in document42" --document my.txt --id document42`

The released language remains experimental; no universal formal proof or human nonprogrammer usability study has been done.
