"""Serializers for the tracker app.

Note: if you use MongoDB ObjectId fields, convert them to strings in the serializer representation.
For example:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = str(instance.id)
        return data
"""
