import unittest

from payer_contract_checker.models import Record
from payer_contract_checker.scoring import score_record


class DepthCheck11(unittest.TestCase):
    def test_011_edge_case_review(self):
        record = Record(id="line-011", exposure=50200, signal=0.599, urgency=2)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
