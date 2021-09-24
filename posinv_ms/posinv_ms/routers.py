class AppRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'invpos_ms':
            return 'invpos_ms'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'invpos_ms':
            return 'invpos_ms'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'invpos_ms' or obj2._meta.app_label == 'invpos_ms':
            return 'invpos_ms'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'invpos_ms':
            return db == 'invpos_ms'
        return db == 'default'
