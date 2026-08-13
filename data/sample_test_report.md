# Mock test
## Checking jets
### If Jets are ready to be assembled
**Summary:** 1 passed, 1 failed

| Test Name                       | Status | Duration |
|---------------------------------|--------|----------|
| get_all_possible_materials      | Pass   | 1.2s     |
| get_all_engines_types           | Fail   | 0.8s     |


### Findings
- `get_all_engines_types` failed: expected key `"Ramjet"` was not present in the returned dict
- Missing entries: `"Experimental High-Speed / Interceptor Concepts"`, `"Ramjet"`


### Code snipet
```python
def check_fuel(fuel_level: float):
    if fuel_level >= 500:
        print("Full")
    else:
        print("Needs fuel")
```


> All tests must pass before contacting supply chain

---
