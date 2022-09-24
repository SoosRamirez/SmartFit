'use strict';

window.onload = function() {
	
	document.onclick = function(e) {
		var target = e.target;

		if (target.classList.contains('popup_closer') ||
			target.classList.contains('popup')) {
			document.querySelector('.popup.active').classList.remove('active');
		};

		if (target.classList.contains('popup_vhod_opener')) {
			document.querySelector('.popup_vhod').classList.add('active');
		};

		if (target.classList.contains('popup_podpiska_opener')) {
			document.querySelector('.popup_podpiska').classList.add('active');
		};

		if (target.classList.contains('popup_smenit_parol_opener')) {
			e.preventDefault();
			document.querySelector('.popup_smenit_parol').classList.add('active');
		};

		if (target.classList.contains('popup_exit_opener')) {
			e.preventDefault();
			document.querySelector('.popup_exit').classList.add('active');
		};

		if (target.classList.contains('programmy_swtchr') &&
			!target.classList.contains('active')) {
			document.querySelector('.programmy_swtchr.active').classList.remove('active');
			target.classList.add('active');

			document.querySelector('.part.active').classList.remove('active');
			document.querySelector('.part_' + target.dataset.num).classList.add('active');
		}

		if (target.classList.contains('napravlenie_swtchr') &&
			!target.classList.contains('active')) {
			document.querySelector('.napravlenie_swtchr.active').classList.remove('active');
			target.classList.add('active');

			document.querySelector('.napravlenie.active').classList.remove('active');
			document.querySelector('.napravlenie_' + target.dataset.num).classList.add('active');
		};

		if (target.classList.contains('parambox_saver') &&
			target.previousSibling.previousSibling.value != '') {
			e.preventDefault();

			document.querySelector('.parambox_' + target.dataset.num).classList.remove('not_filled');
			document.querySelector('.parambox_' + target.dataset.num + '_value').innerHTML = target.previousSibling.previousSibling.value;
		} else if (target.classList.contains('parambox_saver') &&
				   target.previousSibling.previousSibling.value == '') {
			e.preventDefault();

			target.previousSibling.previousSibling.classList.add('error');
		}

		if (target.classList.contains('parambox_changer')) {
			document.querySelector('.parambox_' + target.dataset.num).classList.add('not_filled');
		}

		if (target.classList.contains('progress_format_swtchr') &&
			!target.classList.contains('active')) {
			document.querySelector('.progress_format_swtchr.active').classList.remove('active');
			target.classList.add('active');

			document.querySelector('.lk_progress .photos.active').classList.remove('active');
			document.querySelector('.lk_progress .photos_' + target.dataset.num).classList.add('active')
		};

		if (target.classList.contains('napravlenie_opener')) {
			document.querySelector('.napravlenie.active').classList.add('open');
		};

		if (target.classList.contains('blog_opener')) {
			document.querySelector('.blog_main').classList.add('open');
		}

		if (target.classList.contains('faq_el')) {
			document.querySelector('.faq_el.active').classList.remove('active');
			target.classList.add('active');
		} else if (target.parentNode.classList.contains('faq_el')) {
			document.querySelector('.faq_el.active').classList.remove('active');
			target.parentNode.classList.add('active');
		}
	};
};