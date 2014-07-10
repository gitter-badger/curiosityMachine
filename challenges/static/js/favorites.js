
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
			$.post(target.attr('data-clear-url')).done( function (result) {
				if (result.success) {
					me.unfavorited(target);
				}
			});
		}
		else {
			$.post(target.attr('data-set-url')).done( function (result) {
				if (result.success) {
					me.favorited(target);
				}
			});
		}
	},

	unfavorited: function (target) {
		// var icon = target.find('span.icon');
		target.find('.favorite-badge-content').removeClass('active');
		target.find('.favorite-badge-icon-plus').removeClass('hide');
		target.removeClass("favorited");
		// icon.removeClass("glyphicon-minus").addClass("glyphicon-plus");
	},

	favorited: function (target) {
		// var icon = target.find('span.icon');
		target.find('.favorite-badge-content').addClass('active');
		target.find('.favorite-badge-icon-plus').addClass('hide');
		target.addClass("favorited");
		// icon.removeClass("glyphicon-plus").addClass("glyphicon-minus");
	}
};



$(document).ready(function () {
	CM.Favorite.Handlers.init();
});