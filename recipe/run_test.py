import sys
from subprocess import call

FAIL_UNDER = "63"  # was 90 before #4
COV = ["coverage"]
RUN = ["run", "--source=hatch_mypyc", "--branch", "-m"]
PYTEST = ["pytest", "-vv", "--color=yes", "--tb=long"]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

SKIPS = [
    # added in
    #   - https://github.com/conda-forge/hatch-mypyc-feedstock/pull/4
    # likely due to:
    #   - https://github.com/ofek/hatch-mypyc/pull/38
    "build_dir",
    "dependency",
    "exclude",
    "exclusion",
    "separation",
    "src_layout",
]


SKIP_OR = " or ".join(SKIPS)
K = ["-k", f"not ({SKIP_OR})"]


if __name__ == "__main__":
    sys.exit(
        # run the tests
        call([*COV, *RUN, *PYTEST, *K])
        # maybe run coverage
        or call([*COV, *REPORT])
    )
