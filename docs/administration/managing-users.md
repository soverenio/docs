# Managing Users

## Team management

Whenever you log into [Soveren](https://app.soveren.io), you are directed to the main page which has a menu on the left. Clicking on your user email within this menu leads you to the [team management page](https://app.soveren.io/team/list):

![Empty team](../../img/administration/team-init.png "Empty team")

A user who is a Soveren admin has the ability to [invite new users](#inviting-a-new-user), generate password recovery links for users who have forgotten their credentials, block other users' access, and configure the [single sign-on (SSO)](#single-sign-on-sso) :

![Team management](../../img/administration/team-existing-user-menu.png "Team management")

## Inviting a new user

You can create new users for your Soveren account by clicking the **Invite** button. This action prompts the following dialog:

![Inviting new user](../../img/administration/team-invite.png "Inviting new user")

Soveren authenticates the user using the email address you provide, and the password they choose upon their first login.

After inputting the new user's email address, click on the **Generate invite link** button, copy the link, and manually send it to the new user via your preferred communication channels, such as email or Slack.

!!! warning "The new user will not receive the invitation link automatically. You must manually send it using your preferred communication channels like Slack or email."

Until the new user accepts the invitation, you have the option to **Revoke** it if you change your mind:

![Revoking the invite of a new user](../../img/administration/team-new-user-menu.png "Revoking the invite of a new user")

Upon clicking the invitation link, the new user is presented with the following form to fill out:

![Creating new user](../../img/administration/team-invite-accept.png "Creating new user")

!!! info "What if a user forgets their password?"

    If a user forgets their password, an admin can issue a password reset link. If you are the only user and have forgotten your password, please contact us at [support@soveren.io](mailto:support@soveren.io), and we will assist by sending you a reset link.

## Single sign-on (SSO)

User authentication with single sign-on (SSO) can be enabled in Soveren, allowing you to manage user access through your own identity provider (IdP). Currently, Soveren supports SSO with OpenID Connect (OIDC).

To begin, you will need to create an OIDC app integration for Soveren within your IdP — essentially, registering the Soveren app. The process to achieve this depends on your IdP. During this process, you will require the redirect URL (also referred to as the reply URL) of Soveren: this is the location to which your IdP directs users after successful registration or authentication. Soveren provides two URLs for this:

* https://auth.soveren.io/ui/login/register/externalidp/callback

* https://auth.soveren.io/ui/login/login/externalidp/callback

Next, navigate to [Soveren's SSO settings](https://app.soveren.io/team/settings) and complete the following form:

![SSO settings](../../img/administration/sso-settings.png "SSO settings")

From your IdP, you need to provide the following parameters:

* **Client ID**: The client ID of the Soveren app as registered within your IdP.
* **Client secret**: The client secret of the Soveren app as registered within your IdP.
* **Issuer**: The URL uniquely identifying your IdP. For instance, for Okta, the Issuer typically takes the form `https://your-domain-admin.okta.com`.

Subsequently, specify the **Email domain** to be authenticated through SSO. You can add more than one domain. For example, if you specify `your-domain.io`, all users with the login email of the form `user@your-domain.io` will be authenticated by your IdP through SSO.

!!! warning "Personal login credentials will no longer work for users subject to single sign-on"

After completing the form and saving the settings, [invite new users](#inviting-a-new-user) from the domain(s) you've configured. Soveren will attempt to authenticate these users through SSO. (It is essential that these users are correctly configured in the IdP.)

!!! danger "Soveren retains the user's refresh token for 24 hours"

    Soveren ensures that a user's refresh token is not older than 24 hours. Consequently, if a user is blocked in the IdP, there might be a delay before their access is revoked in Soveren.
