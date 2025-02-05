from docs_snippets.concepts.ops_jobs_graphs.unit_tests import (
    test_event_stream,
    test_inputs_op_with_invocation,
    test_job,
    test_job_with_config,
    test_op_resource_def,
    test_op_with_context,
    test_op_with_invocation,
)


def test_unit_tests():
    test_job()
    test_op_with_invocation()
    test_op_with_context()
    test_job_with_config()
    test_event_stream()
    test_inputs_op_with_invocation()
    test_op_resource_def()
