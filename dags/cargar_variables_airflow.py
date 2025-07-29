from airflow.models import Variable

org = Variable.get("organization")
foo_json = Variable.get("foo_baz", deserialize_json=True)