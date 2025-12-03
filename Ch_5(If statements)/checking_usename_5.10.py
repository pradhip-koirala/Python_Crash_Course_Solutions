current_users = ['michel','jimmy','charls','sofia','lamine']

new_users = ['messi','sofia','ronaldo','carlson','jimmy']

for user in new_users:
    if user.lower() in current_users:
        print("\nUsername already exit.",user)
        print("You need to enter new username.\n")
    else:
        print("\nUsername is available.",user)

