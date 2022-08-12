import {MDCTopAppBar} from '@material/top-app-bar';
import {MDCFormField} from '@material/form-field';
import {MDCRadio} from '@material/radio';
import {MDCTabBar} from '@material/tab-bar';
import {MDCMenu} from '@material/menu';
import {MDCTextField} from '@material/textfield';

// Instantiation
const topAppBarElement = document.querySelector('.mdc-top-app-bar');
const topAppBar = new MDCTopAppBar(topAppBarElement);

const tabBar = new MDCTabBar(document.querySelector('.mdc-tab-bar'));

const menu = new MDCMenu(document.querySelector('.mdc-menu'));
menu.open = true;



const radio = new MDCRadio(document.querySelector('.mdc-radio'));
const formField = new MDCFormField(document.querySelector('.mdc-form-field'));
formField.input = radio;




const textField = new MDCTextField(document.querySelector('.mdc-text-field'));


