# AIC onboarding homework: Hello World

A small practice repository for learning Git, GitHub Actions and the AWS console
before we work on the real project. Nothing here touches the team repository.

- `hello_aws.py` writes a greeting to your own S3 bucket and reads it back.
- `test_hello.py` tests it without needing AWS; GitHub Actions runs it on every pull request.
- `.github/workflows/ci.yml` is the GitHub Actions workflow. Read it, it is short.

Follow the homework handout from your team leader for the step-by-step instructions.

Rules: never commit AWS keys or a `.env` file, only use buckets whose names start
with `aic-hw-`, and delete your bucket when you are done.
