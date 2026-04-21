def detect_suspicious_activity(domain, count):
    sensitive_domains = ["google.com", "facebook.com", "instagram.com"]

    if count > 8:
        return f"ALERT: High DNS traffic detected for {domain}"

    if domain in sensitive_domains:
        return f"Monitoring sensitive domain: {domain}"

    return f"Normal activity for {domain}"
