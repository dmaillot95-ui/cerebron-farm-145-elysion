import pathlib,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"training"))
from source_gate import admit

class SourceGateTests(unittest.TestCase):
    def test_gold_validated_passes(self):
        self.assertTrue(admit({"memory_class":"M4_GOLD","validated":True,"object_path":"elysion/M4/x"})[0])
    def test_m6_class_fails(self):
        self.assertFalse(admit({"memory_class":"M6_COLD_BENCHMARK","validated":True,"object_path":"elysion/M6/x"})[0])
    def test_m6_path_fails_even_if_mislabeled_gold(self):
        self.assertFalse(admit({"memory_class":"M4_GOLD","validated":True,"object_path":"elysion/M6/x"})[0])
    def test_raw_agora_fails(self):
        self.assertFalse(admit({"memory_class":"RAW_AGORA","validated":True,"object_path":"agora/raw/x"})[0])
    def test_unverified_external_fails(self):
        self.assertFalse(admit({"memory_class":"UNVERIFIED_EXTERNAL","validated":False,"object_path":"external/x"})[0])
    def test_replay_requires_promotion(self):
        self.assertFalse(admit({"memory_class":"M2_REPLAY_PROMOTED","validated":True,"promoted":False,"object_path":"elysion/M2/x"})[0])
        self.assertTrue(admit({"memory_class":"M2_REPLAY_PROMOTED","validated":True,"promoted":True,"object_path":"elysion/M2/x"})[0])

if __name__=="__main__":
    unittest.main()
