var Greek = {
	view: function(vnode){
		return m('span', betaCodeToGreek(vnode.attrs.text));
	}
}

var Row = {
	view: function(vnode) {
		return m('.row', vnode.children);
	}
}

var Column = {
	view: function(vnode) {
		return m('div',{class : "column"}, vnode.children);
	}
}
