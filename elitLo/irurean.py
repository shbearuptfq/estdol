# Define constants for better readability and maintainability
ONE_ETHER = 10**18
THIRTY_DAYS_IN_SECONDS = 60 * 60 * 24 * 30

# Build the transaction with the optimized parameters
contract_txn = contract.functions.stake(
    amount=ONE_ETHER,  # Using the constant for 1 ether
    lock_period=THIRTY_DAYS_IN_SECONDS,  # Using the constant for 30 days
).buildTransaction({
    'nonce': nonce,  # Ensure keys are in quotes
    'gasPrice': gas_price,  # Use consistent key formatting
    'gas': gas,  # Use consistent key formatting
})
