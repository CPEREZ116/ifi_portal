app_name = "ifi_portal"
app_title = "IFI Portal"
app_publisher = "Cruzada Estudiantil y Profesional de Colombia"
app_description = "Plataforma financiera IFI sobre ERPNext"
app_email = "cesar.perezv@cruzadaestudiantil.org"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ifi_portal",
# 		"logo": "/assets/ifi_portal/logo.png",
# 		"title": "IFI Portal",
# 		"route": "/ifi_portal",
# 		"has_permission": "ifi_portal.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ifi_portal/css/ifi_portal.css"
# app_include_js = "/assets/ifi_portal/js/ifi_portal.js"

# include js, css files in header of web template
# web_include_css = "/assets/ifi_portal/css/ifi_portal.css"
# web_include_js = "/assets/ifi_portal/js/ifi_portal.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ifi_portal/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ifi_portal/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "ifi_portal.utils.jinja_methods",
# 	"filters": "ifi_portal.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ifi_portal.install.before_install"
# after_install = "ifi_portal.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ifi_portal.uninstall.before_uninstall"
# after_uninstall = "ifi_portal.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ifi_portal.utils.before_app_install"
# after_app_install = "ifi_portal.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ifi_portal.utils.before_app_uninstall"
# after_app_uninstall = "ifi_portal.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "ifi_portal.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ifi_portal.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ifi_portal.tasks.all"
# 	],
# 	"daily": [
# 		"ifi_portal.tasks.daily"
# 	],
# 	"hourly": [
# 		"ifi_portal.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ifi_portal.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ifi_portal.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ifi_portal.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "ifi_portal.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ifi_portal.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ifi_portal.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ifi_portal.utils.before_request"]
# after_request = ["ifi_portal.utils.after_request"]

# Job Events
# ----------
# before_job = ["ifi_portal.utils.before_job"]
# after_job = ["ifi_portal.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ifi_portal.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

app_include_css = [
    "/assets/ifi_portal/css/swiper-bundle.min.css",
    "/assets/ifi_portal/css/ict-theme.css",
    "/assets/ifi_portal/css/ict-layout.css",
    "/assets/ifi_portal/css/ict-components.css",
    "/assets/ifi_portal/css/ict-responsive.css",
]

permission_query_conditions = {
    "Donacion":
        "ifi_portal.security.hooks.donacion_query",

    "Recibo Donacion":
        "ifi_portal.security.hooks.recibo_donacion_query",

    "Planilla":
        "ifi_portal.security.hooks.planilla_query",
}

app_include_js = [
    "/assets/ifi_portal/js/swiper-bundle.min.js",
    "/assets/ifi_portal/js/ict.js",
    "/assets/ifi_portal/js/security.js",
]

fixtures = [
    {
        "dt": "Workspace"
    },
    {
        "dt": "Print Format",
        "filters": [
            ["module", "=", "IFI Portal"]
        ]
    },
    {
        "dt": "Report",
        "filters": [
            ["module", "=", "IFI Portal"]
        ]
    },
    {
        "dt": "Client Script",
        "filters": [
            ["module", "=", "IFI Portal"]
        ]
    },
    {
        "dt": "Server Script"
    },
    {
        "dt": "Workflow"
    }
]


