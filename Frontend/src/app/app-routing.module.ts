import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MsalGuard } from '@azure/msal-angular';
import { BrowserUtils } from '@azure/msal-browser';
import { ProfileComponent } from './profile/profile.component';
import { HomeComponent } from './home/home.component';
import { FailedComponent } from './failed/failed.component';
import { ViewPropertyComponent } from './view-property/view-property.component';
import { AddPropertyComponent } from './add-property/add-property.component';
import { PropertyDetailViewComponent } from './property-detail-view/property-detail-view.component';

const routes: Routes = [
    // {
    //     path: 'profile',
    //     component: ProfileComponent,
    //     canActivate: [MsalGuard]
    // },

    {
        path: 'add',
        component: AddPropertyComponent,
        canActivate: [MsalGuard]
    },
    {
        path: 'view/:id',
        component: PropertyDetailViewComponent
    },
    {
        path: 'login-failed',
        component: FailedComponent
    },
    {
        path: '',
        component: HomeComponent
    },    
];

@NgModule({
    imports: [RouterModule.forRoot(routes, {
        // Don't perform initial navigation in iframes or popups
        initialNavigation: !BrowserUtils.isInIframe() && !BrowserUtils.isInPopup() ? 'enabledNonBlocking' : 'disabled' // Set to enabledBlocking to use Angular Universal
    })],
    exports: [RouterModule]
})
export class AppRoutingModule { }