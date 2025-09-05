class TestMathOps:
    @classmethod
    def setup_class(cls):
        print("\nSetup resources once for TestMathOps")

    @classmethod
    def teardown_class(cls):
        print("\nTeardown resources once for TestMathOps")

    def test_add(self):
        assert 1 + 2 == 3

    def test_multiply(self):
        assert 2 * 3 == 6
