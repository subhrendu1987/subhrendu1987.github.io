/*
 ADOBE CONFIDENTIAL
 ___________________

 Copyright 2012 Adobe Systems Incorporated
 All Rights Reserved.

 NOTICE:  All information contained herein is, and remains
 the property of Adobe Systems Incorporated and its suppliers,
 if any.  The intellectual and technical concepts contained
 herein are proprietary to Adobe Systems Incorporated and its
 suppliers and may be covered by U.S. and Foreign Patents,
 patents in process, and are protected by trade secret or copyright law.
 Dissemination of this information or reproduction of this material
 is strictly forbidden unless prior written permission is obtained
 from Adobe Systems Incorporated.
*/
(function(a,b,c){c.Plugins.TabbedPanelsPlugin={defaultOptions:{widgetClassName:"TabbedPanelsWidget",tabClassName:"TabbedPanelsTab",tabHoverClassName:"TabbedPanelsTabHover",tabDownClassName:"TabbedPanelsTabDown",tabActiveClassName:"TabbedPanelsTabSelected",panelClassName:"TabbedPanelsContent",panelActiveClassName:"TabbedPanelsContentVisible",defaultIndex:0,canCloseAll:!1},initialize:function(c,f){var g=this;a.extend(f,a.extend({},g.defaultOptions,f));b.Widget.Disclosure.DisplayPropertyTransitionPlugin.initialize(c,
f);c.bind("attach-behavior",function(){g._attachBehavior(c)})},_attachBehavior:function(a){var b=a.tabs?a.tabs.$element:null;if(b&&(b.first().addClass("TabbedPanelsTabFirst"),b.last().addClass("TabbedPanelsTabLast"),a.options.event!=="click"))b.on(a.options.event,function(){a.tabs.selectTab(this)})}};c.Plugins.AccordionPlugin={defaultOptions:{widgetClassName:"AccordionWidget",tabClassName:"AccordionPanelTab",tabHoverClassName:"AccordionPanelTabHover",tabDownClassName:"AccordionPanelTabDown",tabActiveClassName:"AccordionPanelTabOpen",
panelClassName:"AccordionPanelContent",panelActiveClassName:"AccordionPanelContentActive",defaultIndex:0,canCloseAll:!1,transitionDirection:"vertical"},initialize:function(c,f){var g=this;a.extend(f,a.extend({},g.defaultOptions,f));f.toggleStateEnabled=f.canCloseAll;b.Widget.Disclosure.AccordionTransitionPlugin.initialize(c,f);c.bind("transform-markup",function(){g._transformMarkup(c)});c.bind("attach-behavior",function(){g._attachBehavior(c)})},_transformMarkup:function(a){var c=a.$element[0];b.scopedFind(c,
".AccordionPanelContent",a.options.widgetClassName,c).removeClass("AccordionPanelContent colelem").wrap('<div class="AccordionPanelContent colelem"><div class="AccordionPanelContentClip"></div></div>').closest(".AccordionPanelContent").css({width:"100%",position:"relative"})},_attachBehavior:function(a){var c=a.$element[0],a=a.options,g=0,h=a.transitionDirection==="vertical",i=h?"offsetWidth":"offsetHeight",j=h?"width":"height";b.scopedFind(c,".AccordionPanel",a.widgetClassName,c).each(function(){g=
g<this[i]?this[i]:g}).each(function(){g>this[i]&&(this.style[j]=g+"px")})}};b.Widget.TabbedPanels.prototype.defaultPlugins=[c.Plugins.TabbedPanelsPlugin];b.Widget.Accordion.prototype.defaultPlugins=[c.Plugins.AccordionPlugin]})(jQuery,WebPro,Muse,window);
