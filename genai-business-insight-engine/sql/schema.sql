CREATE TABLE accounts (
    account_id VARCHAR PRIMARY KEY,
    account_name VARCHAR,
    industry VARCHAR,
    country VARCHAR,
    signup_date DATE,
    referral_source VARCHAR,
    plan_tier VARCHAR,
    seats INTEGER,
    is_trial BOOLEAN,
    churn_flag BOOLEAN
);

CREATE TABLE churn_events (
    churn_event_id VARCHAR PRIMARY KEY,
    account_id VARCHAR,
    churn_date DATE,
    reason_code VARCHAR,
    refund_amount_usd DECIMAL,
    preceding_upgrade_flag BOOLEAN,
    preceding_downgrade_flag BOOLEAN,
    is_reactivation BOOLEAN,
    feedback_text TEXT,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);
