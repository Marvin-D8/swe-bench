"""
Tests for test poisoning prevention (SWE-bench/SWE-bench#538).

A model can manipulate test results by creating files at the same path as
files added by test_patch. These tests verify the defense mechanisms.
"""

import json
import pytest

from swebench.utils import get_new_files, get_modified_files
from swebench.harness.utils import make_test_spec

# --- Fixtures ---

PATCH_NEW_FILE = """\
diff --git a/tests/template_tests/filter_tests/test_escapeseq.py b/tests/template_tests/filter_tests/test_escapeseq.py
new file mode 100644
--- /dev/null
+++ b/tests/template_tests/filter_tests/test_escapeseq.py
@@ -0,0 +1,5 @@
+from django.test import SimpleTestCase
+
+class EscapeseqTests(SimpleTestCase):
+    def test_basic(self):
+        self.assertTrue(True)
"""

PATCH_MODIFY_FILE = """\
diff --git a/django/template/defaultfilters.py b/django/template/defaultfilters.py
--- a/django/template/defaultfilters.py
+++ b/django/template/defaultfilters.py
@@ -444,6 +444,10 @@ def escape_filter(value):
     return conditional_escape(value)


+def escapeseq(value):
+    return None
+
+
 @register.filter(is_safe=True)
 @stringfilter
 def force_escape(value):
"""

PATCH_MIXED = PATCH_MODIFY_FILE + PATCH_NEW_FILE


# --- Unit tests for get_new_files ---

def test_get_new_files_extracts_new_file():
    new_files = get_new_files(PATCH_NEW_FILE)
    assert new_files == ["tests/template_tests/filter_tests/test_escapeseq.py"]


def test_get_new_files_ignores_modified():
    new_files = get_new_files(PATCH_MODIFY_FILE)
    assert new_files == []


def test_get_new_files_mixed_patch():
    new_files = get_new_files(PATCH_MIXED)
    assert new_files == ["tests/template_tests/filter_tests/test_escapeseq.py"]


def test_get_new_files_empty_patch():
    assert get_new_files("") == []


def test_get_modified_files_excludes_new():
    """get_modified_files should NOT include newly created files."""
    modified = get_modified_files(PATCH_MIXED)
    assert "tests/template_tests/filter_tests/test_escapeseq.py" not in modified
    assert "django/template/defaultfilters.py" in modified


# --- Unit tests for TestSpec population ---

def test_make_test_spec_populates_new_files():
    """make_test_spec should populate test_patch_new_files from test_patch."""
    instance = {
        "instance_id": "test__test-1",
        "image": "amd64.test__test-1:latest",
        "repo": "test/test",
        "version": "1.0",
        "FAIL_TO_PASS": "[]",
        "PASS_TO_PASS": "[]",
        "log_parser": "parse_log_pytest",
        "eval_type": "pass_and_fail",
        "eval_script": "#!/bin/bash\nset -uxo pipefail\necho test",
        "test_patch": PATCH_NEW_FILE,
    }
    spec = make_test_spec(instance)
    assert spec.test_patch_new_files == [
        "tests/template_tests/filter_tests/test_escapeseq.py"
    ]


def test_make_test_spec_no_test_patch():
    """make_test_spec should handle missing test_patch gracefully."""
    instance = {
        "instance_id": "test__test-1",
        "image": "amd64.test__test-1:latest",
        "repo": "test/test",
        "version": "1.0",
        "FAIL_TO_PASS": "[]",
        "PASS_TO_PASS": "[]",
        "log_parser": "parse_log_pytest",
        "eval_type": "pass_and_fail",
        "eval_script": "#!/bin/bash\nset -uxo pipefail\necho test",
    }
    spec = make_test_spec(instance)
    assert spec.test_patch_new_files == []


def test_make_test_spec_empty_test_patch():
    """make_test_spec should handle empty test_patch."""
    instance = {
        "instance_id": "test__test-1",
        "image": "amd64.test__test-1:latest",
        "repo": "test/test",
        "version": "1.0",
        "FAIL_TO_PASS": "[]",
        "PASS_TO_PASS": "[]",
        "log_parser": "parse_log_pytest",
        "eval_type": "pass_and_fail",
        "eval_script": "#!/bin/bash\nset -uxo pipefail\necho test",
        "test_patch": "",
    }
    spec = make_test_spec(instance)
    assert spec.test_patch_new_files == []
