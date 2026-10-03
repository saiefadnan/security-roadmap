SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="${1:-$SCRIPT_DIR/sample_auth.log}"

echo "===================================="
echo "Linux Authentication Log Analyzer"
echo "===================================="
echo ""
echo "Analyzing log: $LOG_FILE"
echo ""

echo "[!] Top Offending IPs (Failed Passwords):"
grep -i "failed password" "$LOG_FILE" | awk '{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' | sort | uniq -c | sort -nr | head -n 10

echo ""
echo "[!] Top Targeted Usernames:"
grep -i "failed password" "$LOG_FILE" | awk '{for(i=1;i<=NF;i++) if($i=="for") { if($(i+1)=="invalid" && $(i+2)=="user") print $(i+3); else print $(i+1) }}' | sort | uniq -c | sort -nr | head -n 10
echo "===================================="