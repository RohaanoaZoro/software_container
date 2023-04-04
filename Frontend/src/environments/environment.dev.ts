export const environment = {
    production: false,
    msalConfig: {
        auth: {
            clientId: '1022e47f-5c7e-4ee6-9563-cd5276fc716e',
        }
    },
    apiConfig: {
        scopes: ["https://devopsuva.onmicrosoft.com/scopes/my-api-scope1"],
        uri: "https://devopsuva.onmicrosoft.com/api-endpoint"
    },
    b2cPolicies: {
        names: {
            signUpSignIn: "b2c_1_susi",
            resetPassword: "b2c_1_reset",
            editProfile: "b2c_1_edit_profile"
        },
        authorities: {
            signUpSignIn: {
                authority: 'https://devopsuva.b2clogin.com/devopsuva.onmicrosoft.com/b2c_1_susi'
            },
            resetPassword: {
                authority: 'https://devopsuva.b2clogin.com/devopsuva.onmicrosoft.com/b2c_1_reset'
            },
            editProfile: {
                authority: "https://devopsuva.b2clogin.com/devopsuva.onmicrosoft.com/b2c_1_edit_profile"
            }
        },
        authorityDomain: "devopsuva.b2clogin.com"
    }
};
