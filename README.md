# GETITMON — commercial project research and focused technical work

**New: Austin next-trade project briefs.** Find commercial project records that
may signal a later service need, such as access control after an office remodel
or cleaning after a tenant finish-out. Every entry separates recorded facts from
inferences and links its source. [Read the three-project sample](COMMERCIAL-SIGNALS-SAMPLE.md).
The proposed pilot is $99 for one scoped brief; these are research signals, not
confirmed buyers or open bids.

Have a CSV import that keeps failing, or a small Python script that produces
the wrong result? Request a scoped, AI-assisted repair with reproducible checks.

## Paid pilot offers

| Service | Starting price (USD) | Proposed deliverable |
| --- | ---: | --- |
| Austin commercial project brief | $99 | Up to ten source-linked project signals for one agreed service niche |
| CSV import diagnosis | $49 | A validation report, explanation of the errors, and a repeatable local check |
| Small Python bug fix | $149 | One focused patch, a regression test, and run instructions |

These are starting prices for small jobs, not automatic checkout purchases.
Final scope, price, turnaround, payment method, and data handling must be agreed
before a job is accepted. No active payment checkout is connected here yet.
This is a new service; no customer results or sales history are claimed.

## Request a scope review

[Open a work request](https://github.com/baba59p/getitmon-services/issues/new?template=work-request.yml). Describe the
expected result, the observed failure, and your deadline. Use a **synthetic or
public example only**: GitHub issues are public. Do not attach customer records,
credentials, or confidential source code. A private transfer method must be
agreed before any non-public material is provided.

The offer covers files and software you own or have permission to use. It does
not include security intrusion, bypassing access controls, fabricated reports,
paid scraping access, or work that requires purchasing third-party services.

## Inspect the sample

The `sample/` folder contains a small offline CSV quality checker and tests.
Run with Python 3.10 or later; no third-party packages or network calls needed:

```sh
python sample/check_csv.py sample/example.csv
python -m unittest discover -s sample -p 'test_*.py' -v
```

The example intentionally contains one bad-width row. The checker reports its
record number and exits with status 1. It never prints cell contents. This is a
demonstration of testable delivery, not a full import compatibility guarantee.

All work is AI-assisted and must be checked against the agreed acceptance criteria.
