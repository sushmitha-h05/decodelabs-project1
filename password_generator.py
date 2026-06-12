import secrets        
import string          
import math            


LETTERS    = string.ascii_letters   
DIGITS     = string.digits          
SYMBOLS    = string.punctuation     

def display_banner():
    print("=" * 55)
    print("   🔐 DECODELABS PASSWORD GENERATOR 🔐")
    print("   Powered by secrets module — NIST 2024 compliant")
    print("=" * 55)

def calculate_entropy(length: int, pool_size: int) -> float:
    """E = L × log2(R) — Information Entropy Formula"""
    return length * math.log2(pool_size)

def get_strength_label(entropy: float) -> str:
    if entropy < 40:
        return "⚠️  WEAK"
    elif entropy < 60:
        return "🟡 MODERATE"
    elif entropy < 80:
        return "🟢 STRONG"
    else:
        return "🔵 VERY STRONG"

def generate_password(length: int, use_symbols: bool) -> str:
    """
    PROCESS PHASE: Build the character pool and generate password.
    Uses secrets.choice() — NOT random.choice() — for true
    cryptographic randomness (hardware-level OS entropy source).
    Uses ''.join(list) pattern for O(N) memory efficiency.
    """
    # Build character pool based on user preference
    pool = LETTERS + DIGITS
    if use_symbols:
        pool += SYMBOLS

    
    required = [
        secrets.choice(LETTERS),
        secrets.choice(DIGITS),
    ]
    if use_symbols:
        required.append(secrets.choice(SYMBOLS))

    remaining = [secrets.choice(pool) for _ in range(length - len(required))]

 
    all_chars = required + remaining
    secrets.SystemRandom().shuffle(all_chars)

 
    return ''.join(all_chars)

def run_generator():
    display_banner()


    while True:
        try:
            length = int(input("\nEnter password length (min 8, recommended 16+): "))
            if length < 8:
                print("❌  Minimum length is 8. NIST recommends 15+ for security.")
                continue
            if length > 128:
                print("❌  Maximum length is 128.")
                continue
            break
        except ValueError:
            print("❌  Invalid input. Enter a whole number.")

    sym_input = input("Include special symbols? (!@#$...) [y/n]: ").strip().lower()
    use_symbols = sym_input == 'y'

    how_many = input("How many passwords to generate? [default: 1]: ").strip()
    count = int(how_many) if how_many.isdigit() and int(how_many) > 0 else 1

    pool_size = 52 + 10 + (32 if use_symbols else 0)
    entropy   = calculate_entropy(length, pool_size)
    strength  = get_strength_label(entropy)

    print("\n" + "=" * 55)
    print(f"   📊 Security Report")
    print(f"   Pool Size  : {pool_size} characters")
    print(f"   Entropy    : {entropy:.1f} bits  {strength}")
    print("=" * 55)

    for i in range(count):
        password = generate_password(length, use_symbols)
        label = f"Password {i+1}" if count > 1 else "Your Password"
        print(f"\n   🔑 {label}:  {password}")

    print("\n" + "=" * 55)
    print("   ✅ Generated using secrets module (NIST 2024 compliant)")
    print("=" * 55)


if __name__ == "__main__":
    run_generator()