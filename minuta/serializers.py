from rest_framework import serializers

from .models import Empresa, Proyecto, Asistente, Minuta, Tema, Definicion, Responsabilidad, Programador, Hora, Movimiento


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = ('id', 'nombre')


class ProgramadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programador
        fields = ('id', 'nombre', 'apellido', 'mail', 'es_socio')


class HoraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hora
        fields = ('id', 'programador', 'proyecto', 'cantidad_horas', 'descripcion', 'fecha')


class ProyectoSerializer(serializers.ModelSerializer):
    empresa_detalle = serializers.SerializerMethodField()
    programadores_detalle = serializers.SerializerMethodField()

    def get_programadores_detalle(self, obj):
        ser = ProgramadorSerializer(obj.programadores, many=True)
        return ser.data

    def get_empresa_detalle(self, obj):
        ser = EmpresaSerializer(obj.empresa)
        return ser.data

    class Meta:
        model = Proyecto
        fields = ('id', 'nombre', 'empresa', 'programadores', 'horas_presupuestada', 'fecha_limite', 'empresa_detalle', 'programadores_detalle')


class AsistenteSerializer(serializers.ModelSerializer):
    empresa_detalle = serializers.SerializerMethodField()

    def get_empresa_detalle(self, obj):
        ser = EmpresaSerializer(obj.empresa)
        return ser.data

    class Meta:
        model = Asistente
        fields = ('id', 'empresa', 'nombre', 'apellido', 'mail', 'empresa_detalle')


class DefinicionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Definicion
        fields = ('id', 'tema', 'texto')


class TemaSerializer(serializers.ModelSerializer):
    definiciones = DefinicionSerializer(many=True, read_only=True)

    class Meta:
        model = Tema
        fields = ('id', 'minuta', 'titulo', 'definiciones')

        
class ResponsabilidadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responsabilidad
        fields = ('id', 'minuta', 'fecha', 'tarea', 'responsables')


class MovimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movimiento
        fields = ('id', 'concepto', 'monto', 'programador', 'descripcion', 'fecha')


class MinutaSerializer(serializers.ModelSerializer):
    temas = TemaSerializer(many=True, read_only=True)
    asistentes_detalle = serializers.SerializerMethodField()
    responsabilidades = ResponsabilidadSerializer(many=True, read_only=True)


    def get_asistentes_detalle(self, obj):
        ser = AsistenteSerializer(obj.asistentes, many=True)
        return ser.data

    class Meta:
        model = Minuta
        fields = ('id', 'fecha', 'proyecto', 'motivo', 'descripcion', 'asistentes', 'temas', 'asistentes_detalle', 'responsabilidades')
