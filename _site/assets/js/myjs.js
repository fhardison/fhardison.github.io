Vue.component('row', {
	template: `<div class="row"><slot></slot></div>`});

Vue.component('column', {
	template: `<div class="column"><slot></slot></div>`});

Vue.component('textcolumn', {
	template: `<div class="column"><blockquote><slot></slot></blockquote></div>`});

Vue.component('column-comment', {
	template: `<div class="column-comment"><slot></slot></div>`});

Vue.component('column-note', {
	template: `<div class="column-note"><slot></slot></div>`});
Vue.component('text-col', {
	template: `<div class="column"><blockquote><slot></slot></blockquote></div>`});

Vue.component('footnote', {
	props: ['num'],
	template: `<a class="footnote"><sup>{{ num }}</sup><span><slot></slot></span></a>`});
