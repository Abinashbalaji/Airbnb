import streamlit as st
import plotly_express as px
import matplotlib.pyplot as plt
import pandas as pd
import math

df = pd.read_csv("/Users/ABINASH/Desktop/ABINASH DS/VS Code/Airbnb.csv")

st.set_page_config(layout="wide")
st.title(":rainbow[_AIRBNB ANALYSIS_]")
Select = st.sidebar.radio("Select the Option", ["Home", "Data Exploration"])

if Select == "Home":
    with st.sidebar:
            st.header(":red[_Skill:-_]")
            st.write(':blue[ :star: Python scripting]') 
            st.write(':blue[ :star: Data Preprocessing]')
            st.write(':blue[ :star: Visualization]')
            st.write(':blue[ :star: EDA]')
            st.write(':blue[ :star: Streamlit]')
            st.write(':blue[ :star: MongoDb]')
            st.write(':blue[ :star: PowerBI or Tableau]')

    st.header("ABOUT THIS PROJECT")

    st.subheader(":green[1. Data Collection:]")

    st.write("""Gather data from Airbnb public API or other available sources.
        Collect information on listings, hosts, reviews, pricing, and location data.""")
    
    st.subheader(":green[2. Data Cleaning and Preprocessing:]")

    st.write("""Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
        Convert data types, handle duplicates, and standardize formats.""")
    
    st.subheader(":green[3. Exploratory Data Analysis (EDA):]")

    st.write("""Conduct exploratory data analysis to understand the distribution and patterns in the data.
        Explore relationships between variables and identify potential insights.""")
    
    st.subheader(":green[4. Visualization:]")

    st.write("""Create visualizations to represent key metrics and trends.
        Use charts, graphs, and maps to convey information effectively.
        Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.""")
    
    st.subheader(":green[5. Geospatial Analysis:]")

    st.write("""Utilize geospatial analysis to understand the geographical distribution of listings.
        Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.""")


if Select == "Data Exploration":
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["***PRICE ANALYSIS***","***AVAILABILITY ANALYSIS***","***LOCATION BASED***",
                                            "***GEOSPATIAL VISUALIZATION***","***TOP CHARTS***"])
    with tab1:
        st.header("PRICE DIFFERENCE:")
        col1,col2 = st.columns(2)
    
        with col1:
            Country = st.selectbox("Select the Country",df["country"].unique())
            df_1 = df[df["country"] == Country]
            df_1.reset_index(drop= True, inplace = True)

            room_type = st.selectbox("Select the Roomtype", df_1["room_type"].unique())
            df_2 = df[df["room_type"] == room_type]
            df_2.reset_index(drop= True, inplace = True)

            df_bar = pd.DataFrame(df_2.groupby('property_type').agg({'price':'mean','cleaning_fee':'mean','review_scores':'sum','number_of_reviews':'sum'}))
            df_bar.reset_index(inplace = True)

            df_bar = df_bar.sort_values(by='price', ascending=False)

            bar_fig = px.bar(df_bar,x='property_type',y='price',title= "PRICE OF PROPERTY TYPES",hover_data=['cleaning_fee','review_scores','number_of_reviews'],
                             color_discrete_sequence=px.colors.sequential.Magma_r, width=600, height=500)
            st.plotly_chart(bar_fig)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")   

            Property_type = st.selectbox("Select the Property type",df_2["property_type"].unique())
            df_3 = df_2[df_2["property_type"] == Property_type]
            df_3.reset_index(drop= True, inplace = True)

            df_pie = pd.DataFrame(df_3.groupby('host_response_time').agg({'price':'sum','bedrooms':'sum'}))
            df_pie.reset_index(inplace = True)

            df_pie = df_pie.sort_values(by='price', ascending=False)

            pie_fig = px.pie(df_pie,names='host_response_time',values='price',hover_data=['bedrooms'],title="PRICE BASED ON HOST RES_TIME",
                             color_discrete_sequence=px.colors.sequential.Viridis, width=600, height=500)
            st.plotly_chart(pie_fig)

        col1,col2 = st.columns(2)
        with col1:
            host_res_time = st.selectbox("Select the Host Response Time", df_3["host_response_time"].unique())
            df_4 = df_3[df_3["host_response_time"] == host_res_time]
            df_4.reset_index(drop= True, inplace = True)
            st.write("")
            st.write("")

            Bedrooms = st.selectbox("Select the bedrooms count", df_4["bedrooms"].unique())
            df_5 = df_4[df_4["bedrooms"] == Bedrooms]
            df_5.reset_index(drop= True, inplace = True)

            st.write("")
            st.write("")

            
        with col2:

            df5_bar = pd.DataFrame(df_5.groupby('bed_type').agg({'minimum_nights':'min','maximum_nights':'max','price':'mean'}))
            df5_bar.reset_index(inplace = True)

            bar6_fig = px.bar(df5_bar,x='bed_type',y=['minimum_nights','maximum_nights'],title= "MINIMUM AND MAXIMUM NIGHTS",
                              hover_data=['price'],color_discrete_sequence=px.colors.sequential.Electric_r,barmode='group',
                              width=600, height=500)
            st.plotly_chart(bar6_fig)
    with tab2:
        st.header("AVAILABILITY ANALYSIS:")
        col1,col2 = st.columns(2)

        with col1:
            country_a = st.selectbox("Select the Country Name",df["country"].unique())

            df1_a = df[df["country"] == country_a]
            df1_a.reset_index(drop=True, inplace=True)

            property_type_a = st.selectbox("Select the Property Type",df1_a['property_type'].unique())

            df2_a = df1_a[df1_a['property_type'] == property_type_a]
            df2_a.reset_index(drop= True, inplace=True)

            avai_vis_1 = px.sunburst(df2_a, path = ['room_type','bed_type','location.is_location_exact'], values='availability_30',
                                     title= 'AVAILABILITY 30',color_discrete_sequence=px.colors.sequential.Hot_r,
                                     width = 600, height= 500)

            st.plotly_chart(avai_vis_1)
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            avai_vis_2 = px.sunburst(df2_a, path = ['room_type','bed_type','location.is_location_exact'], values='availability_60',
                                     title= 'AVAILABILITY 60',color_discrete_sequence=px.colors.sequential.Brwnyl,
                                     width = 600, height= 500)

            st.plotly_chart(avai_vis_2)   
        with col1:
            avai_vis_3 = px.sunburst(df2_a, path = ['room_type','bed_type','location.is_location_exact'], values='availability_90',
                                     title= 'AVAILABILITY 90',color_discrete_sequence=px.colors.sequential.haline_r,
                                     width = 600, height= 500)

            st.plotly_chart(avai_vis_3)   
        with col2:
            avai_vis_4 = px.sunburst(df2_a, path = ['room_type','bed_type','location.is_location_exact'], values='availability_365',
                                     title= 'AVAILABILITY 365',color_discrete_sequence=px.colors.sequential.Inferno_r,
                                     width = 600, height= 500)

            st.plotly_chart(avai_vis_4)  

        room_type_ = st.selectbox("Select the Room Type", df2_a['room_type'].unique()) 

        df_7 = df2_a[df2_a['room_type'] == room_type_]

        df_7_a = pd.DataFrame(df_7.groupby('host_response_time')[['availability_30','availability_60',
                                                                    'availability_90','availability_365','price']].sum())
        
        df_7_a.reset_index(inplace= True)

        bar7_fig = px.bar(df_7_a,x='host_response_time',y=['availability_30','availability_60','availability_90','availability_365'],title= "AVAILABILITY BY HOST RESPONSE TIME",
                            hover_data=['price'],color_discrete_sequence=px.colors.sequential.haline_r,barmode='group',
                            width=1000, height=500)
        st.plotly_chart(bar7_fig)  

    with tab3:
        st.header("LOCATION BASED:")
        
        df_l = df
        
        country_c = st.radio("Select the Country",df_l['country'].unique())
        df_8 = df_l[df_l["country"] == country_c]
        df_8.reset_index(drop = True,inplace = True)

        Property_type_b = st.radio("Select the Property Type",df_8['property_type'].unique())
        df_9 = df_8[df_8["property_type"] == Property_type_b]
        df_9.reset_index(inplace = True)

        def select_the_df(sel_val):
            if sel_val == str(df_9['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df_9['price'].min())+' '+str("(30% of the Value)"):

                df_val_30= df_9[df_9["price"] <= differ_max_min*0.30 + df_9['price'].min()]
                df_val_30.reset_index(drop= True, inplace= True)
                return df_val_30

            elif sel_val == str(differ_max_min*0.30 + df_9['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df_9['price'].min())+' '+str("(30% to 60% of the Value)"):
            
                df_val_60= df_9[df_9["price"] >= differ_max_min*0.30 + df_9['price'].min()]
                df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df_9['price'].min()]
                df_val_60_1.reset_index(drop= True, inplace= True)
                return df_val_60_1
            
            elif sel_val == str(differ_max_min*0.60 + df_9['price'].min())+' '+str('to')+' '+str(df_9['price'].max())+' '+str("(60% to 100% of the Value)"):

                df_val_100= df_9[df_9["price"] >= differ_max_min*0.60 + df_9['price'].min()]
                df_val_100.reset_index(drop= True, inplace= True)
                return df_val_100
            
        differ_max_min= df_9['price'].max()-df_9['price'].min()

        val_sel= st.radio("Select the Price Range",[str(df_9['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df_9['price'].min())+' '+str("(30% of the Value)"),
                                                    
                                                    str(differ_max_min*0.30 + df_9['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df_9['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                    str(differ_max_min*0.60 + df_9['price'].min())+' '+str('to')+' '+str(df_9['price'].max())+' '+str("(60% to 100% of the Value)")])
                                          
        df_val_sel= select_the_df(val_sel)

        st.dataframe(df_val_sel)

        # checking the correlation

        df_val_sel_corr= df_val_sel.drop(columns=["listing_url","name", "property_type",                 
                                            "room_type", "bed_type","cancellation_policy",
                                            "images","host_url","host_name", "host_location",                   
                                            "host_response_time",            
                                            "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                            "host_picture_url","host_neighbourhood",
                                            "host_identity_verified","host_verifications",
                                            "street", "suburb", "government_area", "market",                        
                                            "country","location.type","location.is_location_exact",
                                            "amenities"]).corr()
        
        st.dataframe(df_val_sel_corr)

        df_val_sel_gr= pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
        df_val_sel_gr.reset_index(inplace= True)

        fig_1= px.bar(df_val_sel_gr, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], title="ACCOMMODATES",
                    hover_data= "extra_people", barmode='group', color_discrete_sequence=px.colors.sequential.Bluyl_r,width=1000)
        st.plotly_chart(fig_1)
        
        
        room_ty_l= st.selectbox("Select the Room_Type_l", df_val_sel["room_type"].unique())

        df_val_sel_rt= df_val_sel[df_val_sel["room_type"] == room_ty_l]

        fig_2= px.bar(df_val_sel_rt, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
                    hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Greens_r,
                    width=1000,height=600)

        st.plotly_chart(fig_2)

        fig_3= px.bar(df_val_sel_rt, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
                    hover_data= ["location.type"], barmode='group', color_discrete_sequence=px.colors.sequential.Blugrn_r,width=1000)
        st.plotly_chart(fig_3)

    with tab4:
        st.header("GEOSPATIAL VISUALIZATION:")

        fig_4 = px.scatter_mapbox(df, lat='latitude',lon='longitude',color_continuous_scale='Viridis',
                                  color='price', size='accommodates',hover_name='name',range_color=(0,255), 
                                  mapbox_style="carto-positron",zoom=1)
        
        fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
        st.plotly_chart(fig_4)   
    with tab5:
        
        country_d = st.selectbox("Select the Country_",df["country"].unique())
        df_t = df[df["country"]==country_d]
        
        property_ty_2 = st.selectbox("Select the Property Type_", df_t["property_type"].unique())
        df_t1 = df[df["property_type"]==property_ty_2]

        df_t1.reset_index(drop=True, inplace=True)

        df_sorted = df_t1.sort_values(by="price")
        df_sorted.reset_index(inplace = True)

        df_b = pd.DataFrame(df_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_b.reset_index(inplace = True)
        df_b.columns = ["host_neighbourhood","Total Price","Average Price"]
        df_b_bar = df_b.sort_values(by='Total Price', ascending=False).head(20)
        df_b_bar11 = df_b.sort_values(by='Average Price', ascending=False).head(20)
        col1, col2 = st.columns(2)

        with col1:

            df_b_bar1 = px.bar(df_b_bar,x="host_neighbourhood", y="Total Price", height= 600,width=600, 
                               title="TOP 20 TOTAL PRICE OF HOST NEIGNBOURHOOD",color_discrete_sequence=px.colors.sequential.Sunset)
        
            st.plotly_chart(df_b_bar1)
        
        with col2:

            df_b_bar2 = px.bar(df_b_bar11,x="host_neighbourhood", y="Average Price", height= 600,width=600, 
                               title="TOP 20 AVERAGE PRICE OF HOST NEIGNBOURHOOD",color_discrete_sequence=px.colors.sequential.Sunsetdark_r)
            

            st.plotly_chart(df_b_bar2)
        
        
        df_b1 = pd.DataFrame(df_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
        df_b1.reset_index(inplace = True)
        df_b1.columns = ["host_location","Total Price","Average Price"]
        df_b1_bar = df_b1.sort_values(by='Total Price', ascending=False).head(20)
        df_b1_bar.head(10)
        df_b1_bar11 = df_b1.sort_values(by='Average Price', ascending=False).head(20)
        
        col1, col2 = st.columns(2)
        with col1:

            df_b1_bar1 = px.bar(df_b1_bar,x="host_location", y="Total Price", height= 600,width=600, 
                            title="TOP 20 TOTAL PRICE OF HOST LOCATION",color_discrete_sequence=px.colors.sequential.Sunset)
        
            st.plotly_chart(df_b1_bar1)
        
        with col2:

            df_b1_bar2 = px.bar(df_b1_bar11,x="host_location", y="Average Price", height= 600,width=600, 
                            title="TOP 20 AVERAGE PRICE OF HOST LOCATION",color_discrete_sequence=px.colors.sequential.Sunsetdark_r)
            

            st.plotly_chart(df_b1_bar2)

        room_ty_2 = st.selectbox("Select the Room Type_", df_t1["room_type"].unique())
        df_r1 = df[df["room_type"]==room_ty_2]

        df_r1.reset_index(drop=True, inplace=True)

        df_sorted1 = df_r1.sort_values(by="price",ascending=False).head(50)
        df_sorted1.reset_index(inplace = True)

        bar_p = px.bar(df_sorted1,x="name", y="price", height= 800,width=600, 
                            title="MIN & MAX NIGHTS AND ACCOMODATES",
                            color_discrete_sequence=px.colors.sequential.Bluyl_r,
                            hover_data=['minimum_nights','maximum_nights','accommodates'])
        st.plotly_chart(bar_p)

        bar_p1 = px.bar(df_sorted1,x="name", y="price", height= 800,width=600, 
                            title="CLEANING FEE, BEDROOMS, BEDS AND EXTRA PEOPLE ",
                            color_discrete_sequence=px.colors.sequential.Bluyl_r,
                            hover_data=["cleaning_fee","bedrooms","beds","extra_people"])
        st.plotly_chart(bar_p1)
























