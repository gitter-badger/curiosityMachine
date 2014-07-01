
CM.Favorite = {Handlers: {}};

CM.Favorite.Handlers =  {
	init: function () {
		this.initListeners()
	},

	initListeners: function () {
		$('.favorite').click({me: this}, this.callback);
	},

	callback: function (e) {
		e.preventDefault();

		var me = e.data.me;
		var target = $(e.currentTarget);
		if ( target.hasClass("favorited") ) {
			$.post(target.attr('data-clear-url')).done( function () { 
				me.unfavorited(target);
			});
		}
		else {
			$.post(target.attr('data-set-url')).done( function () { 
				console.log(me);
				me.favorited(target);
			});
		}
	},

	unfavorited: function (target) {
		var icon = target.find('span');
		target.removeClass("favorited");
		icon.removeClass("glyphicon-star").addClass("glyphicon-star-empty");
	},

	favorited: function (target) {
		var icon = target.find('span');
		target.addClass("favorited");
		icon.addClass("glyphicon-star").removeClass("glyphicon-star-empty");
	}
};



$(document).ready(function () {
	CM.Favorite.Handlers.init();
});