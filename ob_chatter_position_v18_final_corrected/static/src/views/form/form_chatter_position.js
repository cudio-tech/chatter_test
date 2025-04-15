/** @odoo-module **/

import { FormController } from "@web/views/form/form_controller";
import { patch } from "@web/core/utils/patch";

patch(FormController.prototype, {
    slideChattter() {
        if ($('body').hasClass("o_chatter_position_normal")) {
            $('body').addClass('o_chatter_position_sided').removeClass('o_chatter_position_normal');
        } else {
            $('body').removeClass('o_chatter_position_sided').addClass('o_chatter_position_normal');
        }
    },
});