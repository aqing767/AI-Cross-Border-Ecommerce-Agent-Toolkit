import json,subprocess,sys,tempfile,unittest
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
class StudioTests(unittest.TestCase):
 def test_scaffold_and_validate(self):
  with tempfile.TemporaryDirectory() as d:
   subprocess.run([sys.executable,str(BASE/"scripts/scaffold_project.py"),"--name","Test Drama","--slug","test-drama","--output",d],check=True,capture_output=True,text=True)
   project=Path(d)/"test-drama"
   r=subprocess.run([sys.executable,str(BASE/"scripts/validate_project.py"),str(project)],capture_output=True,text=True)
   self.assertEqual(r.returncode,0,r.stdout+r.stderr)
   data=json.loads((project/"project.json").read_text())
   self.assertEqual(data["project_id"],"test-drama")
 def test_refuses_overwrite(self):
  with tempfile.TemporaryDirectory() as d:
   subprocess.run([sys.executable,str(BASE/"scripts/scaffold_project.py"),"--name","Test","--slug","test-drama","--output",d],check=True,capture_output=True)
   r=subprocess.run([sys.executable,str(BASE/"scripts/scaffold_project.py"),"--name","Test","--slug","test-drama","--output",d],capture_output=True,text=True)
   self.assertNotEqual(r.returncode,0)
if __name__=="__main__":unittest.main()
