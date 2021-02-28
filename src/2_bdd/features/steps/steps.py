from behave import step

@step('sum "{a:d}" with "{b:d}"')
def test_sum(context, a, b):
    context.result = a + b

@step('the result should be "{result:d}"')
def test_sum(context, result):
    assert context.result == result
