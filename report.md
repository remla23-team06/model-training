# ML Project Report
**Project** | **Details**
--------|--------
Date    | Wed, 31 May 2023 09:09:42 +0200 
Path    | `/Users/rkargul/Documents/university/REMLA/restaurant/model-training`
Config  | `pyproject.toml`
Default | No
Git: Remote URL | `git@github.com:remla23-team06/model-training.git`
Git: Commit     | `862aab4eeb0a82b38da5ddbe0be32d8115ad7a45`
Git: Branch     | `A4-ml-config-manag`
Git: Dirty Workspace?  | Yes
Number of Python files | 5
Lines of Python code   | 72

---

## Config

**Note** — The following rules were disabled in `mllint`'s configuration:
- `version-control/code/git`
- `dependency-management`
- `testing/pass`
- `testing/coverage`

## Reports

### Version Control (`version-control`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | DVC: Project uses Data Version Control | `version-control/data/dvc`
✅ | 100.0% | 1 | DVC: Is installed | `version-control/data/dvc-is-installed`
✅ | 100.0% | 1 | DVC: Folder '.dvc' should be committed to Git | `version-control/data/commit-dvc-folder`
✅ | 100.0% | 1 | DVC: Should have at least one remote data storage configured | `version-control/data/dvc-has-remote`
✅ | 100.0% | 1 | DVC: Should be tracking at least one data file | `version-control/data/dvc-has-files`
✅ | 100.0% | 1 | DVC: File 'dvc.lock' should be committed to Git | `version-control/data/commit-dvc-lock`
 | _Total_ | | | 
✅ | **100.0**% | | Version Control | `version-control`

### Code Quality (`code-quality`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
✅ | 100.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
✅ | 100.0% | 1 | Pylint reports no issues with this project | `code-quality/pylint/no-issues`
✅ | 100.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
✅ | 100.0% | 1 | Mypy reports no issues with this project | `code-quality/mypy/no-issues`
✅ | 100.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
✅ | 100.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
✅ | 100.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
✅ | 100.0% | 1 | Bandit reports no issues with this project | `code-quality/bandit/no-issues`
 | _Total_ | | | 
✅ | **100.0**% | | Code Quality | `code-quality`

#### Details — Project should use code quality linters — ✅

Hooray, all linters detected:

- Mypy
- Black
- isort
- Bandit
- Pylint


#### Details — Pylint reports no issues with this project — ✅

Congratulations, Pylint is happy with your project!

#### Details — Mypy reports no issues with this project — ✅

Congratulations, Mypy is happy with your project!

#### Details — Black reports no issues with this project — ✅

Congratulations, Black is happy with your project!

#### Details — isort reports no issues with this project — ✅

Congratulations, `isort` is happy with your project!

#### Details — Bandit reports no issues with this project — ✅

Congratulations, Bandit is happy with your project!

### Testing (`testing`) — **50.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project has automated tests | `testing/has-tests`
✅ | 100.0% | 1 | Tests should be placed in the tests folder | `testing/tests-folder`
 | _Total_ | | | 
❌ | **50.0**% | | Testing | `testing`

#### Details — Project has automated tests — ✅

Great! Your project contains **1** test file, which meets the minimum of **1** test files required.

This equates to **20%** of Python files in your project being tests, which meets the target ratio of **20%**

### Continuous Integration (`ci`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project uses Continuous Integration (CI) | `ci/use`
 | _Total_ | | | 
✅ | **100.0**% | | Continuous Integration | `ci`

