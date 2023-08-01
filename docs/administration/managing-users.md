# Managing Users

## Team Management

Whenever you log into [Soveren](https://app.soveren.io), you are directed to the main page which has a menu on the left. Clicking on your user email within this menu leads you to the [team management page](https://app.soveren.io/team/list):

![Empty team](../../img/administration/team-init.png "Empty team")

A user who is a Soveren admin has the ability to [invite new users](#inviting-a-new-user), generate password recovery links for users who have forgotten their credentials, block other users' access, and configure the [single sign-on (SSO)](#single-sign-on-sso) :

![Team management](../../img/administration/team-existing-user-menu.png "Team management")

## Inviting a New User

You can create new users for your Soveren account by clicking the **Invite** button. This action prompts the following dialog:

![Inviting new user](../../img/administration/team-invite.png "Inviting new user")

Soveren authenticates the user using the email address you provide, and the password they choose upon their first login.

After inputting the new user's email address, click on the **Generate invite link** button, copy the link, and manually send it to the new user via your preferred communication channels, such as email or Slack.

!!! warning "The new user will not receive the invitation link automatically. You must manually send it using your preferred communication channels like Slack or email."

Until the new user accepts the invitation, you have the option to **Revoke** it if you change your mind:

![Revoking the invite of a new user](../../img/administration/team-new-user-menu.png "Revoking the invite of a new user")

Upon clicking the invitation link, the new user is presented with the following form to fill out:

![Creating new user](../../img/administration/team-invite-accept.png "Creating new user")


## Single sign-on (SSO)

