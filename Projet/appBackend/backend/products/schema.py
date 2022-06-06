from itertools import product
from unicodedata import decimal
import graphene
from graphene_django import DjangoObjectType
from .models import Category,Laptoop

class CategoryType(DjangoObjectType):
    class Meta: 
        model = Category
        fields = ('id','title')

  
class LaptoopType(DjangoObjectType):
    class Meta: 
        model = Laptoop
        fields = (
            'id',
            'Manufacturer',
            'Model_Name',
            'Category',
            'Screen_Size', 
            'Screen',
            'CPU', 
            'RAM',
            'Storage',
            'GPU',
            'Operating_System',
            'Weight',
            'Price'
           

        )  


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    laptops = graphene.List(LaptoopType)

    def resolve_laptops(root, info, **kwargs):
        # Querying a list
        return Laptoop.objects.all()

    def resolve_categories(root, info, **kwargs):
        # Querying a list
        return Category.objects.all()

schema = graphene.Schema(query=Query)

class UpdateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to update a category 
        title = graphene.String(required=True)
        id = graphene.ID()


    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title, id):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()
        
        return UpdateCategory(category=category)

class CreateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        title = graphene.String(required=True)

    # Class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title):
        category = Category()
        category.title = title
        category.save()
        
        return CreateCategory(category=category)

class LaptoopInput(graphene.InputObjectType):
    Manufacturer= graphene.String()
    Model_Name = graphene.String()
    Category = graphene.String()
    Screen_Size = graphene.String()
    Screen = graphene.String()
    CPU = graphene.String()
    RAM = graphene.String()
    Storage = graphene.String()
    GPU = graphene.String()
    Operating_System = graphene.String()
    Weight = graphene.String()
    Price = graphene.String()



class CreateLaptoop(graphene.Mutation):
    class Arguments:
        input = LaptoopInput(required=True)

    laptoop = graphene.Field(LaptoopType)
    
    @classmethod
    def mutate(cls, root, info, input):
        laptoop = Laptoop()
        laptoop.Manufacturer = input.Manufacturer
        laptoop.Model_Name = input.Model_Name
        laptoop.Category = input.Category
        laptoop.Screen_Size = input.Screen_Size
        laptoop.Screen = input.Screen
        laptoop.CPU = input.CPU
        laptoop.RAM = input.RAM
        laptoop.Storage = input.Storage
        laptoop.GPU = input.GPU
        laptoop.Operating_System = input.Operating_System
        laptoop.Weight = input.Weight
        laptoop.Price = input.Price
        laptoop.save()
        return CreateLaptoop(laptoop=laptoop)

class UpdateLaptop(graphene.Mutation):
    class Arguments:
        input = LaptoopInput(required=True)
        id = graphene.ID()

    book = graphene.Field(LaptoopType)

    @classmethod
    def mutate(cls, root, info, input, id):
        laptop = Laptoop.objects.get(pk=id)
        laptop.Manufacturer = input.Manufacturer
        laptop.Model_Name = input.Model_Name
        laptop.Category = input.Category
        laptop.Screen_Size = input.Screen_Size
        laptop.Screen = input.Screen
        laptop.CPU = input.CPU
        laptop.RAM = input.RAM
        laptop.Storage = input.Storage
        laptop.GPU = input.GPU
        laptop.Operating_System = input.Operating_System
        laptop.Weight = input.Weight
        laptop.Price = input.Price
        laptop.save()
        return UpdateLaptop(laptop=laptop)

class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()
    create_laptop = CreateLaptoop.Field()
    update_Laptop=UpdateLaptop.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)