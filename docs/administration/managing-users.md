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

### Creating an OIDC app integration

To begin, you will need to create an OIDC app integration for Soveren within your IdP — essentially, registering the Soveren app. The process to achieve this depends on your IdP. During this process, you will require the redirect URL (also referred to as the reply URL) of Soveren: this is the location to which your IdP directs users after successful registration or authentication. Soveren provides two URLs for this:

* `https://auth.soveren.io/ui/login/register/externalidp/callback`

* `https://auth.soveren.io/ui/login/login/externalidp/callback`

Next, navigate to [Soveren's SSO settings](https://app.soveren.io/team/settings) and complete the following form:

![SSO settings](../../img/administration/sso-settings.png "SSO settings")

### Configuring the SSO authentication

From your IdP, you need to provide the following parameters:

* **Client ID**: The client ID of the Soveren app as registered within your IdP.
* **Client secret**: The client secret of the Soveren app as registered within your IdP.

### Configuring the SSO provider

The settings here depend on whether you are using Active Directory Federation Services (ADFS) or another OIDC provider.

![SSO provider: OIDC](../../img/administration/sso-provider-oidc.png "SSO provider: OIDC")

For an OIDC provider, **Issuer** refers to the URL that uniquely identifies your IdP. For example, in the case of Okta, the Issuer typically takes the form `https://your-domain-admin.okta.com`.

Specifically for ADFS, however, you need to provide more parameters:

![SSO provider: ADFS](../../img/administration/sso-provider-adfs.png "SSO provider: ADFS")

* **Authorization endpoint**: This is a URL used for ADFS authentication.
* **Token endpoint**: This endpoint is used to exchange an authorization code for access and refresh tokens.

### Configuring the domain

Specify the **Email domain** to be authenticated through SSO. You can add multiple domains. For example, if you specify `your-domain.io`, all users with an email address in the format `user@your-domain.io` will be authenticated by your IdP through SSO.

!!! warning "Personal login credentials will no longer work for users subject to single sign-on"

### Managing users

There are two options for adding new users to Soveren through SSO: manually inviting selected users or fully delegating user management to your IdP.

If you [invite new users](#inviting-a-new-user) from the domain(s) you've configured, Soveren will attempt to authenticate these users through SSO. (It is crucial that these users are correctly configured in the IdP.)

!!! danger "Soveren checks if the user is active in the IdP at least once every 24 hours"

    If a user is blocked in the IdP, there might be up to a 24-hour delay before their access is revoked in Soveren.

However, if you prefer not to manually invite users, you can delegate user management to your IdP:

![SSO settings: delegate user management](../../img/administration/sso-settings-delegate.png "SSO settings: delegate user management")

Soveren will automatically create new users when they log in for the first time. The authorization of the user to access Soveren is determined by your IdP.
