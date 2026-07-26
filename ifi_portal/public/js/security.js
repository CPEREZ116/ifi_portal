window.ifi = window.ifi || {};
ifi.security = ifi.security || {};

ifi.security.filter_unit_field = function(frm, fieldname){

    frm.set_query(fieldname, function(){

        return {

            query:
                "ifi_portal.security.api.link_query"

        };

    });

};

