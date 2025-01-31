# Bus-Asymmetric-Encryption 🚌🔐

## Preface 

This is a simple asymmetric encryption algorithm conceived during a bus ride on **January 31, 2025**.  
While documenting this idea, **I do NOT recommend using this algorithm** due to potential undiscovered flaws. However, its simplicity is notable—part of it relies on linear transformations.

---

## Core Idea 💡

1. **Key Pair Generation**  
   - Take a 256-digit integer `A`, create its reversed copy `B`.  
   - Compute `C` by summing the product of corresponding digits from `A` and `B`.  
     (Example: `24` → `24` and `42` → `2×4 + 4×2 = 8 + 8 = 16`)  
   - Treat `A` as a digit sequence (e.g., `231` → `[2, 3, 1]`), sort it to get sequence `D` (e.g., `[1, 2, 3]`), then convert it back to an integer (e.g., `123`).  
   - Compute a new value by multiplying and summing digits of `D` and `C` (method similar to above).  

2. **Padding & Expansion**  
   - To extend short `C` and `D`:  
     Find the largest prime factor `X` of `A` not exceeding `100`, multiply `C` and `D` by `X` to get `C'` and `D'`.  
   - Pad `C'` and `D'` cyclically with digits `0-9` to 128 bits, then reprocess.  
   - Use the final `C'` and `D'` as the public key for Unicode encryption.  

---

## Performance Tests 🧪

Refer to [`Effect_Testing.py`](./Effect_Testing.py) for implementation.  
*(Note: Custom test functions were used; potential misunderstandings in algorithm details might affect accuracy.)*

### Test Results
- **Key Sensitivity**  
  - Hamming Distance: `66`  
  - Bit Change Rate: `51.56%`  

- **Encryption Speed**  
  - `1KB` data: `0.0002 seconds`  
  - `10KB` data: `0.0091 seconds`  
  - `100KB` data: `0.1442 seconds`  

- **Collision Resistance**  
  - Passed with `1,000,000 iterations` and `1,000-length` texts.  
  *(Larger-scale tests not performed.)*  

- **Edge Cases**  
  - Passed tests for `1MB` data, empty strings, and single-character inputs.  

---

## Final Notes 📝

While simple and computationally lightweight, this algorithm may have undiscovered vulnerabilities. Use it for experimental purposes only. Feedback and improvements are welcome!  

🚀 Happy Hacking!  
